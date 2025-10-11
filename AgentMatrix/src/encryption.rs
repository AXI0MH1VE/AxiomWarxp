use aes_gcm::{
    aead::{Aead, KeyInit},
    Aes256Gcm, Error, Key, Nonce,
};

pub fn encrypt(data: &[u8], key: &[u8]) -> Result<Vec<u8>, Error> {
    let key = Key::<Aes256Gcm>::from_slice(key);
    let cipher = Aes256Gcm::new(key);
    let nonce = Nonce::from_slice(b"unique nonce"); // In practice, use random nonce
    let ciphertext = cipher.encrypt(nonce, data)?;
    Ok(ciphertext)
}

pub fn decrypt(ciphertext: &[u8], key: &[u8]) -> Result<Vec<u8>, Error> {
    let key = Key::<Aes256Gcm>::from_slice(key);
    let cipher = Aes256Gcm::new(key);
    let nonce = Nonce::from_slice(b"unique nonce");
    let plaintext = cipher.decrypt(nonce, ciphertext)?;
    Ok(plaintext)
}
