import "./styles/CreateUser.css";
import { create_athlete } from "../api/admin/athlete";
import { create_officer } from "../api/admin/officer";
import { getToken } from "../api/utility/utility";
import { useState } from "react";

function CreateUser() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [isAdmin, setIsAdmin] = useState(false);
  const [hasKiloAccess, setHasKiloAccess] = useState(false);
  const [password, setPassword] = useState("");

  const token = getToken() || ""; // fallback to empty string if null

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!token) {
      console.error("No token available!");
      return;
    }

    if (isAdmin) {
      await create_officer(token, firstName, lastName, isAdmin, hasKiloAccess, password);
    } else {
      await create_athlete(token, firstName, lastName, isAdmin, hasKiloAccess);
    }

    // Reset form
    setFirstName("");
    setLastName("");
    setIsAdmin(false);
    setHasKiloAccess(false);
    setPassword("");
  };

  return (
    <div className="create-user-container">
      <form className="create-user-form" onSubmit={handleSubmit}>
        <h2>Create User</h2>

        <label>First Name:</label>
        <input
          type="text"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          required
        />

        <label>Last Name:</label>
        <input
          type="text"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          required
        />

        <fieldset>
          <legend>Admin Status:</legend>
          <label>
            <input
              type="radio"
              checked={isAdmin === true}
              onChange={() => setIsAdmin(true)}
            />
            Yes
          </label>
          <label>
            <input
              type="radio"
              checked={isAdmin === false}
              onChange={() => setIsAdmin(false)}
            />
            No
          </label>
        </fieldset>

        <fieldset>
          <legend>Kilo Access:</legend>
          <label>
            <input
              type="radio"
              checked={hasKiloAccess === true}
              onChange={() => setHasKiloAccess(true)}
            />
            Yes
          </label>
          <label>
            <input
              type="radio"
              checked={hasKiloAccess === false}
              onChange={() => setHasKiloAccess(false)}
            />
            No
          </label>
        </fieldset>

        {isAdmin && (
          <>
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </>
        )}

        <button type="submit">Create User</button>
      </form>
    </div>
  );
}

export default CreateUser;
