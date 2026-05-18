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
        renderStats();
        renderCompare();
        renderShiftTables();
    } else {
        showError("Data not loaded. Please run 'python build_static_data.py' first.");
    }

    function renderDashboard() {
        const metadata = scanReport.metadata || {};
        const results = scanReport.results || {};

        document.getElementById('files-scanned').textContent = metadata.files_scanned || 0;
        document.getElementById('total-violations').textContent = metadata.total_violations || 0;
        
        let speedup = "0.00x";
        if (metadata.naive_time && metadata.horspool_time && metadata.horspool_time > 0) {
            speedup = (metadata.naive_time / metadata.horspool_time).toFixed(2) + "x";
        }
        document.getElementById('speedup').textContent = speedup;

        const filesList = document.getElementById('files-list');
        const fileNames = Object.keys(results);

        if (fileNames.length === 0) {
            filesList.innerHTML = `<div class="empty-state"><p>No issues found in the scanned codebase.</p></div>`;
            return;
        }

        filesList.innerHTML = '';
        fileNames.forEach(fileName => {
            const issues = results[fileName];
            const fileCard = document.createElement('div');
            fileCard.className = 'file-card';
            
            fileCard.innerHTML = `
                <div class="file-header">
                    <span class="file-title">${escapeHtml(fileName)}</span>
                    <span class="file-badge">${issues.length} issue${issues.length !== 1 ? 's' : ''}</span>
                </div>
                <ul class="violation-list">
                    ${issues.map(issue => `
                        <li class="violation-item">
                            <div class="v-line">L${issue.line}</div>
                            <div class="v-content">
                                <div class="v-title">
                                    <span class="v-severity sev-${issue.severity.toLowerCase()}">${issue.severity}</span>
                                    <span class="v-pattern">"${escapeHtml(issue.pattern)}"</span>
                                </div>
                                <div class="v-context sev-${issue.severity.toLowerCase()}-border">${escapeHtml(issue.context)}</div>
                            </div>
                        </li>
                    `).join('')}
                </ul>
            `;
            filesList.appendChild(fileCard);
        });
    }

    function renderStats() {
        const metadata = scanReport.metadata || {};
        const results = scanReport.results || {};
        const sev = metadata.severity_counts || {};

        // Find worst offending file
        let worstFile = "N/A";
        let worstCount = 0;
        for (const [fname, issues] of Object.entries(results)) {
            if (issues.length > worstCount) {
                worstCount = issues.length;
                worstFile = fname;
            }
        }

        // Find most common patterns
        const patternFreq = {};
        for (const issues of Object.values(results)) {
            for (const issue of issues) {
                patternFreq[issue.pattern] = (patternFreq[issue.pattern] || 0) + 1;
            }
        }
        
        let mostCommon = "N/A";
        let mostCommonCount = 0;
        const sortedPatterns = Object.entries(patternFreq).sort((a, b) => b[1] - a[1]);
        if (sortedPatterns.length > 0) {
            mostCommon = sortedPatterns[0][0];
            mostCommonCount = sortedPatterns[0][1];
        }

        // Populate Overview
        document.getElementById('stats-overview').innerHTML = `
            <li><span class="stats-label">Files Scanned</span><span class="stats-val">${metadata.files_scanned || 0}</span></li>
            <li><span class="stats-label">Files w/ Issues</span><span class="stats-val">${Object.keys(results).length}</span></li>
            <li><span class="stats-label">Total Violations</span><span class="stats-val">${metadata.total_violations || 0}</span></li>
            <li><span class="stats-label">Critical Issues</span><span class="stats-val" style="color: var(--accent-red)">${sev.critical || 0}</span></li>
            <li><span class="stats-label">Warnings</span><span class="stats-val" style="color: var(--accent-yellow)">${sev.warning || 0}</span></li>
            <li><span class="stats-label">Style Issues</span><span class="stats-val" style="color: var(--accent-blue)">${sev.style || 0}</span></li>
        `;

        // Populate Insights
        document.getElementById('stats-insights').innerHTML = `
            <li><span class="stats-label">Worst File</span><span class="stats-val">${escapeHtml(worstFile)} (${worstCount})</span></li>
            <li><span class="stats-label">Top Pattern</span><span class="stats-val">"${escapeHtml(mostCommon)}" (${mostCommonCount})</span></li>
            <li><span class="stats-label">Horspool Time</span><span class="stats-val">${(metadata.horspool_time || 0).toFixed(5)}s</span></li>
            <li><span class="stats-label">Naive Time</span><span class="stats-val">${(metadata.naive_time || 0).toFixed(5)}s</span></li>
            <li><span class="stats-label">Scan Duration</span><span class="stats-val">${(metadata.scan_time || 0).toFixed(5)}s</span></li>
        `;

        // Populate Top Patterns Table
        const tbody = document.querySelector('#top-patterns-table tbody');
        tbody.innerHTML = sortedPatterns.slice(0, 10).map(([pattern, count]) => `
            <tr>
                <td style="font-family: monospace">"${escapeHtml(pattern)}"</td>
                <td style="text-align: right; font-weight: 600">${count}</td>
            </tr>
        `).join('');
    }

    function renderCompare() {
        if (typeof fileComparisons === 'undefined') return;

        // Extract unique files
        const fileSet = new Set();
        Object.keys(fileComparisons).forEach(key => {
            const [f1, f2] = key.split('|');
            fileSet.add(f1);
            fileSet.add(f2);
        });

        const files = Array.from(fileSet).sort();
        const sel1 = document.getElementById('compare-file1');
        const sel2 = document.getElementById('compare-file2');

        files.forEach(f => {
            sel1.add(new Option(f, f));
            sel2.add(new Option(f, f));
        });

        const handleCompare = () => {
            const f1 = sel1.value;
            const f2 = sel2.value;
            const resDiv = document.getElementById('compare-results');
            
            if (!f1 || !f2) {
                resDiv.classList.add('hidden');
                return;
            }

            if (f1 === f2) {
                resDiv.innerHTML = `
                    <div class="sim-label">Comparing identical files</div>
                    <div class="sim-score sim-high">100%</div>
                    <p style="color: var(--text-muted)">Same file selected.</p>
                `;
                resDiv.classList.remove('hidden');
                return;
            }

            // Look up the precomputed score (key could be f1|f2 or f2|f1)
            let comp = fileComparisons[`${f1}|${f2}`] || fileComparisons[`${f2}|${f1}`];
            
            if (comp) {
                let simLevel = "Low Similarity";
                let simClass = "sim-low";
                if (comp.similarity >= 80) {
                    simLevel = "High Similarity - Possible Plagiarism";
                    simClass = "sim-high";
                } else if (comp.similarity >= 50) {
                    simLevel = "Moderate Similarity";
                    simClass = "sim-mod";
                }

                resDiv.innerHTML = `
                    <div class="sim-label">Similarity Score</div>
                    <div class="sim-score ${simClass}">${comp.similarity}%</div>
                    <div style="font-weight: 600; color: var(--text-main); margin-bottom: 12px;">${simLevel}</div>
                    <p style="color: var(--text-muted)">Longest Common Substring length: <strong>${comp.lcs} characters</strong></p>
                `;
            } else {
                resDiv.innerHTML = `<p style="color: var(--accent-yellow)">Comparison data not found for these files.</p>`;
            }
            resDiv.classList.remove('hidden');
        };

        sel1.addEventListener('change', handleCompare);
        sel2.addEventListener('change', handleCompare);
    }

    function renderShiftTables() {
        const patterns = Object.keys(shiftTables);
        const select = document.getElementById('shifttable-select');
        const display = document.getElementById('shifttable-display');

        if (patterns.length === 0) {
            select.disabled = true;
            display.innerHTML = '<p class="empty-state">No shift tables found.</p>';
            return;
        }

        // Populate dropdown
        patterns.forEach(pattern => {
            select.add(new Option(pattern, pattern));
        });

        const showPattern = (pattern) => {
            const data = shiftTables[pattern];
            if (!data) return;

            let tableHtml = `
                <div class="table-card">
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

            const sortedChars = Object.keys(data.table);
            sortedChars.forEach(char => {
                tableHtml += `
                    <tr>
                        <td>'${escapeHtml(char)}'</td>
                        <td>${data.table[char]}</td>
                    </tr>
                `;
            });

            tableHtml += `
                        <tr>
                            <td class="st-other">*(other)</td>
                            <td class="st-other">${data.length}</td>
                        </tr>
                    </tbody>
                    </table>
                </div>
            `;
            
            display.innerHTML = tableHtml;
        };

        // Initialize with first pattern
        showPattern(patterns[0]);

        select.addEventListener('change', (e) => {
            showPattern(e.target.value);
        });
    }

    function escapeHtml(unsafe) {
        if (!unsafe) return "";
        return String(unsafe)
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
