import { useEffect } from "react"

function App() {
  
  async function fetchHelloWorld() {
    const response = await fetch("http://localhost:8000/")
    const data = await response.json()
    console.log(data)
  }
  
  useEffect(() => {
    fetchHelloWorld()
  }, [])
  
  return (
    <div>
      <h1 className="text-3xl font-bold underline">
        Hello world!
      </h1>
    </div>
  )
}

export default App
