import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Login = () => {
	const { store, actions } = useContext(Context);
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const token = sessionStorage.getItem("token");

	const handleClick = () => {
		const opts = {
			method: "POST",
			headers:{
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"username": username,
				"password": password
			})
		}
		fetch("https://glowing-goldfish-jjr6gjqxxwrgfqx6g-3001.app.github.dev/api/token", opts)
			.then(resp => {
				if(resp.status === 200) resp.json();
				else alert("there has been some error");
			})
			.then(data => {
				sessionStorage.setItem("token", data.access_token)
			})
			.catch(error => {
				console.error("there was an error", error)
			})
	}
	return (
		<div className="text-center mt-5">
			<h1>Login</h1>
			{(token && token != "" && token != undefined) ? "You are looged in with this token" + token :
			<div>

				<input type="text" placeholder="username" value={username} onChange={(e) => setUsername(e.target.value)}></input>
				<input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)}></input>
				<button onClick={handleClick}>Login</button>
			</div>
			}
		</div>
	);
};
