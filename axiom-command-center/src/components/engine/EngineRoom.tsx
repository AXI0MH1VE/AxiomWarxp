import React, { useState } from 'react';
import { invoke } from '@tauri-apps/api/core';

const EngineRoom: React.FC = () => {
  const [kernelOutput, setKernelOutput] = useState('');
  const [testOutput, setTestOutput] = useState('');
  const [abmvOutput, setAbmvOutput] = useState('');

  const handleStartKernel = async () => {
    try {
      const result = await invoke<string>('start_kernel');
      setKernelOutput(result);
    } catch (error) {
      setKernelOutput(`Error: ${error}`);
    }
  };

  const handleRunTest = async () => {
    try {
      const result = await invoke<string>('run_constellation_test');
      setTestOutput(result);
    } catch (error) {
      setTestOutput(`Error: ${error}`);
    }
  };

  const handleRunAbmv = async () => {
    const plan = JSON.stringify({ Project_Name: "Test Plan", Strategy: { Monetization_Strategy: "Monetize_later" } });
    try {
      const result = await invoke<string>('run_abmv', { plan });
      setAbmvOutput(result);
    } catch (error) {
      setAbmvOutput(`Error: ${error}`);
    }
  };

  return (
    <div>
      <h1>Engine Room</h1>
      <button onClick={handleStartKernel}>Start Kernel</button>
      <pre>{kernelOutput}</pre>
      <button onClick={handleRunTest}>Run Constellation Test</button>
      <pre>{testOutput}</pre>
      <button onClick={handleRunAbmv}>Run ABMV</button>
      <pre>{abmvOutput}</pre>
    </div>
  );
};

export default EngineRoom;
