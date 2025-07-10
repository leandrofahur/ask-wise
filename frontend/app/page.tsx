"use client"
import { FaGithub } from "react-icons/fa";
import FSMGraph from "@/components/FSMGraph/FSMGraph";
import { getFSM } from "@/lib/api";

import React, { useState } from "react";

async function postFSM(fsm: any) {
  await fetch("http://localhost:8000/api/v1/fsm", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(fsm),
  });
}

export default function Home() {
  const [fsm, setFsm] = React.useState<any | null>(null);
  const [form, setForm] = useState({
    initial_state: "",
    states: "",
    marked_states: "",
    events: "",
    transitions: "",
  });
  const [loading, setLoading] = useState(false);

  React.useEffect(() => {
    getFSM().then(setFsm).catch(() => setFsm(null));
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    // Parse form fields
    const states = form.states.split(",").map((s) => s.trim()).filter(Boolean);
    const marked_states = form.marked_states.split(",").map((s) => s.trim()).filter(Boolean);
    const events = form.events.split(",").map((s) => s.trim()).filter(Boolean);
    // transitions: one per line, format: from,event,to
    const transition_function: Record<string, string> = {};
    form.transitions.split("\n").forEach((line) => {
      const [from, event, to] = line.split(",").map((s) => s.trim());
      if (from && event && to) transition_function[`${from}:${event}`] = to;
    });
    const fsmObj = {
      initial_state: form.initial_state,
      states,
      marked_states,
      events,
      transition_function,
    };
    await postFSM(fsmObj);
    setFsm(fsmObj);
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col">
      <main className="flex-1 flex flex-col items-center justify-center py-8">
        <form
          className="w-full max-w-xl bg-white rounded-xl shadow-lg border p-6 mb-8"
          onSubmit={handleSubmit}
        >
          <h2 className="text-lg font-semibold mb-4">Create FSM</h2>
          <div className="mb-3">
            <label className="block text-sm font-medium">Initial State</label>
            <input
              className="w-full border rounded px-2 py-1"
              name="initial_state"
              value={form.initial_state}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label className="block text-sm font-medium">States (comma separated)</label>
            <input
              className="w-full border rounded px-2 py-1"
              name="states"
              value={form.states}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label className="block text-sm font-medium">Marked States (comma separated)</label>
            <input
              className="w-full border rounded px-2 py-1"
              name="marked_states"
              value={form.marked_states}
              onChange={handleChange}
            />
          </div>
          <div className="mb-3">
            <label className="block text-sm font-medium">Events (comma separated)</label>
            <input
              className="w-full border rounded px-2 py-1"
              name="events"
              value={form.events}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label className="block text-sm font-medium">Transitions (one per line: from,event,to)</label>
            <textarea
              className="w-full border rounded px-2 py-1"
              name="transitions"
              value={form.transitions}
              onChange={handleChange}
              rows={4}
              required
            />
          </div>
          <button
            type="submit"
            className="w-full py-2 bg-blue-600 text-white rounded font-semibold hover:bg-blue-700 transition"
            disabled={loading}
          >
            {loading ? "Saving..." : "Save & Visualize FSM"}
          </button>
        </form>
        <div className="w-full max-w-2xl">
          {fsm ? <FSMGraph description={fsm} /> : <div className="text-gray-500">No FSM defined yet.</div>}
        </div>
      </main>
      <footer className="bg-white border-t py-4 text-center text-gray-500 mt-auto">
        <a
          className="inline-flex items-center gap-2 hover:underline"
          href="https://github.com/leandrofahur/ask-wise/tree/main"
          target="_blank"
          rel="noopener noreferrer"
        >
          <FaGithub />
          <span>View on GitHub</span>
        </a>
        <div>© 2025 Leandro Fahur</div>
      </footer>
    </div>
  );
}
