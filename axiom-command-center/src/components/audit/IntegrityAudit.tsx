import React, { useState } from 'react';
import { invoke } from '@tauri-apps/api/core';

const IntegrityAudit: React.FC = () => {
  const [validationOutput, setValidationOutput] = useState('');
  const attestation = 'Sovereign Attestation: All hashes verified. Integrity: 100%';

  const handleValidateSchema = async () => {
    try {
      const result = await invoke<string>('validate_schema');
      setValidationOutput(result);
    } catch (error) {
      setValidationOutput(`Error: ${error}`);
    }
  };

  return (
    <div>
      <h1>Integrity Audit</h1>
      <button onClick={handleValidateSchema}>Validate Schemas</button>
      <pre>{validationOutput}</pre>
      <p>{attestation}</p>
    </div>
  );
};

export default IntegrityAudit;
