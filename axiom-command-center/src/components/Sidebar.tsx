import React from 'react';

interface SidebarProps {
  activeSection: string;
  onSectionChange: (section: string) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ activeSection, onSectionChange }) => (
  <aside className="sidebar">
    <nav>
      <ul>
        {['mission', 'engine', 'doctrine', 'ops', 'audit', 'settings'].map(section => (
          <li key={section}>
            <button
              className={activeSection === section ? 'active' : ''}
              onClick={() => onSectionChange(section)}
            >
              {section.toUpperCase().replace('_', ' ')}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  </aside>
);
