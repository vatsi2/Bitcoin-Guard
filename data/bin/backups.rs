use tokio::fs;
use tokio::time::{sleep, Duration};

async fn backup_task(path: &str) {
    loop {
        sleep(Duration::from_secs(86400)).await; // Каждые 24 часа
        fs::copy(path, "/backup/vault.bin").await.unwrap();
    }
}
