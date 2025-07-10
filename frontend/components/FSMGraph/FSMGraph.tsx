"use client"
import React from 'react';
import Mermaid from 'react-mermaid2';

interface FSMDescription {
  initial_state: string;
  states: string[];
  marked_states: string[];
  events: string[];
  transition_function: Record<string, string>;
}

const mapDescriptionToMermaid = (fsm: FSMDescription): string => {
  const lines: string[] = ['stateDiagram-v2'];
  lines.push(`[*] --> ${fsm.initial_state}`);
  for (const [key, toState] of Object.entries(fsm.transition_function)) {
    const [fromState, event] = key.split(':');
    lines.push(`${fromState} --> ${toState}: ${event}`);
  }  
  return lines.join('\n');
};

const FSMGraph = ({ description }: { description: FSMDescription }) => {
  const mermaidCode = mapDescriptionToMermaid(description);
  return (
    <div>
      <Mermaid chart={mermaidCode} />
    </div>
  );
};

export default FSMGraph;