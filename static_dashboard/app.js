document.addEventListener('DOMContentLoaded', () => {
    // Navigation Logic
    const navItems = document.querySelectorAll('.nav-item');
    const viewSections = document.querySelectorAll('.view-section');
    const pageTitle = document.getElementById('page-title');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = item.getAttribute('data-tab');
            
            // Update active states
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            viewSections.forEach(section => {
                section.classList.remove('active');
                if (section.id === `${tabId}-view`) {
                    section.classList.add('active');
                }
            });

            // Update title
            pageTitle.textContent = item.textContent.trim();
        });
    });

    // Populate Data
    if (typeof scanReport !== 'undefined' && typeof shiftTables !== 'undefined') {
        renderDashboard();
        renderShiftTables();
    } else {
        showError("Data not loaded. Please run 'python build_static_data.py' first.");
    }

    function renderDashboard() {
        const metadata = scanReport.metadata || {};
        const results = scanReport.results || {};

        // Update Metrics
        document.getElementById('files-scanned').textContent = metadata.files_scanned || 0;
        document.getElementById('total-violations').textContent = metadata.total_violations || 0;
        
        let speedup = "0.00x";
        if (metadata.naive_time && metadata.horspool_time && metadata.horspool_time > 0) {
            speedup = (metadata.naive_time / metadata.horspool_time).toFixed(2) + "x";
        }
        document.getElementById('speedup').textContent = speedup;

        // Render Report Analysis
        const filesList = document.getElementById('files-list');
        const fileNames = Object.keys(results);

        if (fileNames.length === 0) {
            filesList.innerHTML = `
                <div class="empty-state">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                    <p>No issues found in the scanned codebase.</p>
                </div>`;
            return;
        }

        filesList.innerHTML = '';
        fileNames.forEach(fileName => {
            const issues = results[fileName];
            
            const fileCard = document.createElement('div');
            fileCard.className = 'file-card';
            
            const header = document.createElement('div');
            header.className = 'file-header';
            header.innerHTML = `
                <span class="file-title">${fileName}</span>
                <span class="file-badge">${issues.length} issue${issues.length !== 1 ? 's' : ''}</span>
            `;
            
            const list = document.createElement('ul');
            list.className = 'violation-list';

            issues.forEach(issue => {
                const li = document.createElement('li');
                li.className = 'violation-item';
                
                // Highlight word in context
                let contextHtml = escapeHtml(issue.context);
                
                li.innerHTML = `
                    <div class="v-line">L${issue.line}</div>
                    <div class="v-content">
                        <div class="v-title">
                            <span class="v-severity sev-${issue.severity.toLowerCase()}">${issue.severity}</span>
                            <span class="v-pattern">"${escapeHtml(issue.pattern)}"</span>
                        </div>
                        <div class="v-context sev-${issue.severity.toLowerCase()}-border">${contextHtml}</div>
                    </div>
                `;
                list.appendChild(li);
            });

            fileCard.appendChild(header);
            fileCard.appendChild(list);
            filesList.appendChild(fileCard);
        });
    }

    function renderShiftTables() {
        const grid = document.getElementById('tables-grid');
        const patterns = Object.keys(shiftTables);

        if (patterns.length === 0) {
            grid.innerHTML = '<p class="empty-state">No shift tables found.</p>';
            return;
        }

        grid.innerHTML = '';
        patterns.forEach(pattern => {
            const data = shiftTables[pattern];
            
            const card = document.createElement('div');
            card.className = 'table-card';
            
            let tableHtml = `
                <div class="table-header">
                    <span class="table-pattern">"${escapeHtml(pattern)}"</span>
                    <span class="v-severity sev-${data.severity.toLowerCase()}">${data.severity}</span>
                </div>
                <table class="st-table">
                    <thead>
                        <tr>
                            <th>Character</th>
                            <th>Shift</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            // Sort table by shift value descending for better UX
            const sortedChars = Object.keys(data.table);

            sortedChars.forEach(char => {
                tableHtml += `
                    <tr>
                        <td>'${escapeHtml(char)}'</td>
                        <td>${data.table[char]}</td>
                    </tr>
                `;
            });

            // Add the *(other) row
            tableHtml += `
                    <tr>
                        <td class="st-other">*(other)</td>
                        <td class="st-other">${data.length}</td>
                    </tr>
                </tbody>
                </table>
            `;
            
            card.innerHTML = tableHtml;
            grid.appendChild(card);
        });
    }

    function escapeHtml(unsafe) {
        if (!unsafe) return "";
        return unsafe
             .replace(/&/g, "&amp;")
             .replace(/</g, "&lt;")
             .replace(/>/g, "&gt;")
             .replace(/"/g, "&quot;")
             .replace(/'/g, "&#039;");
    }

    function showError(msg) {
        document.getElementById('dashboard-view').innerHTML = `
            <div class="empty-state">
                <p style="color: var(--accent-red); font-weight: 500;">${msg}</p>
            </div>
        `;
    }
});
