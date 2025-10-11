import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { invoke } from '@tauri-apps/api/core';

const DoctrineLedger: React.FC = () => {
  const [principlesContent, setPrinciplesContent] = useState('');

  useEffect(() => {
    const loadPrinciples = async () => {
      try {
        const content = await invoke<string>('read_markdown_file', { path: 'AxiomHive/PRINCIPLES.md' });
        setPrinciplesContent(content);
      } catch (error) {
        console.error('Failed to load principles:', error);
        setPrinciplesContent('# Error loading PRINCIPLES.md');
      }
    };
    loadPrinciples();
  }, []);

  return (
    <div>
      <h1>Doctrine Ledger</h1>
      <ReactMarkdown>{principlesContent}</ReactMarkdown>
    </div>
  );
};

export default DoctrineLedger;
