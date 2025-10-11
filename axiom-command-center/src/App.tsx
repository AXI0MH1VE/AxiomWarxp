import { useState } from 'react';
import { Sidebar } from './components/Sidebar';
import MissionControl from './components/mission/MissionControl';
import EngineRoom from './components/engine/EngineRoom';
import DoctrineLedger from './components/doctrine/DoctrineLedger';
import OperationsCenter from './components/ops/OperationsCenter';
import IntegrityAudit from './components/audit/IntegrityAudit';
import SystemSettings from './components/settings/SystemSettings';

function App() {
  const [activeSection, setActiveSection] = useState('mission');

  const renderContent = () => {
    switch (activeSection) {
      case 'mission':
        return <MissionControl />;
      case 'engine':
        return <EngineRoom />;
      case 'doctrine':
        return <DoctrineLedger />;
      case 'ops':
        return <OperationsCenter />;
      case 'audit':
        return <IntegrityAudit />;
      case 'settings':
        return <SystemSettings />;
      default:
        return <MissionControl />;
    }
  };

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <Sidebar activeSection={activeSection} onSectionChange={setActiveSection} />
      <div style={{ flex: 1, padding: '20px' }}>
        {renderContent()}
      </div>
    </div>
  );
}

export default App;
