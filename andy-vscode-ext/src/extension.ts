import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {

    vscode.workspace.onDidSaveTextDocument((doc) => {
        sendEvent({ type: 'vscode_save', file: doc.fileName });
    });

    vscode.debug.onDidStartDebugSession(() => {
        sendEvent({ type: 'vscode_debug_start' });
    });

    vscode.debug.onDidTerminateDebugSession(() => {
        sendEvent({ type: 'vscode_debug_end' });
    });

}

function sendEvent(payload: object) {
    fetch('http://localhost:8000/event', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    }).catch(err => console.error('Andy agent unreachable:', err));
}

export function deactivate() {}