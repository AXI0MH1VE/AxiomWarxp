import React, { useState } from 'react';

const OperationsCenter: React.FC = () => {
  const [deployOutput, setDeployOutput] = useState('');
  const [rollbackOutput, setRollbackOutput] = useState('');

  const handleDeploy = () => {
    setDeployOutput('Deployment initiated. All systems go.');
  };

  const handleRollback = () => {
    setRollbackOutput('Rollback executed. System stable.');
  };

  return (
    <div>
      <h1>Operations Center</h1>
      <button onClick={handleDeploy}>Deploy</button>
      <pre>{deployOutput}</pre>
      <button onClick={handleRollback}>Rollback</button>
      <pre>{rollbackOutput}</pre>
    </div>
  );
};

export default OperationsCenter;
