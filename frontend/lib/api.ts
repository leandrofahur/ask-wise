export async function getFSM() {
    const res = await fetch("http://localhost:8000/fsm");
    if (!res.ok) throw new Error("Failed to fetch FSM");
    return res.json();
  }