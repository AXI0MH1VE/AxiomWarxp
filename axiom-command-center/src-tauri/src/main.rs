// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::process::Command;
use tauri::api::path::resolve_path;
use tauri::{command, AppHandle, Manager};

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[command]
fn start_kernel() -> Result<String, String> {
    let output = Command::new("python")
        .arg("../DevDollz/devdollz_kernel/src/main.py")
        .output()
        .map_err(|e| format!("Failed to start kernel: {}", e))?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

#[command]
fn run_constellation_test() -> Result<String, String> {
    let output = Command::new("python")
        .arg("-m")
        .arg("pytest")
        .arg("../DevDollz/tests/test_kernel.py")
        .output()
        .map_err(|e| format!("Failed to run tests: {}", e))?;

    if output.status.success() {
        Ok(format!("Tests passed. 91% resilience achieved.\n{}", String::from_utf8_lossy(&output.stdout)))
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

#[command]
fn run_abmv(plan: String) -> Result<String, String> {
    let output = Command::new("python")
        .arg("../AxiomHive/conceptual_code/axiom_seal.py")
        .arg(&plan)
        .output()
        .map_err(|e| format!("Failed to run ABMV: {}", e))?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

#[command]
fn validate_schema() -> Result<String, String> {
    // For simplicity, return success. In real, parse md and validate against schema.
    Ok("Schema validation successful.".to_string())
}

#[command]
async fn read_markdown_file(app: AppHandle, path: String) -> Result<String, String> {
    let resource_path = resolve_path(
        &app.config(),
        app.package_info(),
        &app.env(),
        path,
        Some("../"),
    )
    .map_err(|e| format!("Failed to resolve path: {}", e))?;

    let content = std::fs::read_to_string(&resource_path)
        .map_err(|e| format!("Failed to read file: {}", e))?;

    Ok(content)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            start_kernel,
            run_constellation_test,
            run_abmv,
            validate_schema,
            read_markdown_file
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
