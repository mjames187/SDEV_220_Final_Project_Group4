class Club:
    name = "UNDEFINED"
    sponsor = "UNDEFINED"
    startTimeHours = 0
    startTimeMins = 0
    endTimeHours = 0
    endTimeMins = 0
    interest = 0
    def __init__(self, name, sponsor, startTime1, startTime2, endTime1, endTime2):   
        self.name = name
        self.sponsor = sponsor
        self.startTimeHours = startTime1
        self.startTimeMins = startTime2
        self.endTimeHours = endTime1
        self.endTimeMins = endTime2

def interestQuery(club):
    if input("Are you interested in this club? y/n ") == "y":
        club.interest += 1


dndClub = Club("DND Club", "Chad Stewart", 15, 0, 17, 30)
debateClub = Club("Debate Club", "Kayla Vasilko", 16, 30, 18, 0)

print(dndClub.name, dndClub.sponsor, dndClub.startTimeHours, ":", dndClub.startTimeMins, dndClub.endTimeHours, ":", dndClub.endTimeMins, dndClub.interest)

selectedClub = dndClub

interestQuery(selectedClub)

src/app.js

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Create from "./pages/Create";
import Details from "./pages/Details";
import Navbar from "./components/Navbar";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<Create />} />
        <Route path="/details/:id" element={<Details />} />
      </Routes>
    </Router>
  );
}

src/components/navbar.js

import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div style={{ padding: 10, background: "#ddd" }}>
      <Link to="/">Home</Link> |{" "}
      <Link to="/create">Create Pitch</Link>
    </div>
  );
}

src/pages/home.js

import { useState } from "react";
import { Link } from "react-router-dom";

export default function Home() {
  const [pitches, setPitches] = useState([
    {
      id: 1,
      title: "Gaming Club",
      description: "Play games together",
      time: "Monday 3 PM",
      likes: 0
    }
  ]);

  const [filter, setFilter] = useState("");

  const like = (id) => {
    setPitches(
      pitches.map(p =>
        p.id === id? { ...p, likes: p.likes + 1 } : p
      )
    );
  };

  const filtered = pitches.filter(p =>
    p.time.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div>
      <h2>Club Pitches</h2>

      <input
        placeholder=" Filter by time."
        onChange={(e) => setFilter(e.target.value)}
      />

      {filtered.map(p => (
        <div key={p.id} style={{ border: "1px solid black", margin: 10 }}>
          <h3>{p.title}</h3>
          <p>{p.description}</p>
          <p>{p.time}</p>
          <p>Likes: {p.likes}</p>

          <button onClick={() => like(p.id)}>Like</button>
          <Link to={`/details/${p.id}`}> View</Link>
        </div>
      ))}
    </div>
  );
}

src/pages/create.js

import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Create() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [time, setTime] = useState("");

  const navigate = useNavigate();

  const submit = () => {
    console.log({ title, description, time });
    navigate("/");
  };

  return (
    <div>
      <h2>Create Pitch</h2>

      <input placeholder="Club Name" onChange={e => setTitle(e.target.value)} /><br />
      <input placeholder="Description" onChange={e => setDescription(e.target.value)} /><br />
      <input placeholder="Meeting Time" onChange={e => setTime(e.target.value)} /><br />

      <button onClick={submit}>Submit</button>
    </div>
  );
}

src/pages/details.js

return (
    <div>
      <h2>Pitch Details (ID: {id})</h2>

      <h3>Discussion Board</h3>

      {comments.map((c, i) => (
        <p key={i}>- {c}</p>
      ))}

      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Write comment."
      />

      <button onClick={addComment}>Post</button>
    </div>
  );
}

Front-end-Bryant Torres 

print(dndClub.interest)

print(debateClub.name, debateClub.sponsor, debateClub.startTimeHours, ":", debateClub.startTimeMins, debateClub.endTimeHours, ":", debateClub.endTimeMins, debateClub.interest)

selectedClub = debateClub

interestQuery(selectedClub)

print(debateClub.interest)
