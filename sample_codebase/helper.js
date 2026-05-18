// helper.js - Helper utility with violations

function executeCommand(cmd) {
    // CRITICAL: Dangerous execution pattern (matching "exec(")
    let result = exec(cmd);
    
    // WARNING: Fixme comment
    // FIXME: This is vulnerable to command injection!
    
    // STYLE: global variable declaration or goto style patterns
    global.helperName = "SystemHelper";
    
    return result;
}
