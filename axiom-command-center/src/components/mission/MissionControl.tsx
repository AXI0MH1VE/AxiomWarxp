import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { invoke } from '@tauri-apps/api/core';

const MissionControl: React.FC = () => {
  const [strategyContent, setStrategyContent] = useState('');

  useEffect(() => {
    const loadStrategy = async () => {
      try {
        const content = await invoke<string>('read_markdown_file', { path: 'AxiomHive/STRATEGY.md' });
        setStrategyContent(content);
      } catch (error) {
        console.error('Failed to load strategy:', error);
        setStrategyContent('# Error loading STRATEGY.md');
      }
    };
    loadStrategy();
  }, []);

  return (
    <div>
      <h1>Mission Control</h1>
      <div>
        <p>Projected ARR: USD 5M</p>
        <p>Audit Reduction: 95%</p>
      </div>
      <ReactMarkdown>{strategyContent}</ReactMarkdown>
    </div>
  );
};

export default MissionControl;
