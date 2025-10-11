pub fn check_ethics(action: &str) -> bool {
    // Simple ethics check
    !action.contains("harm")
}
