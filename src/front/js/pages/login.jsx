import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Login = () => {
	const { store, actions } = useContext(Context);
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const token = sessionStorage.getItem("token");
	const navigate = useNavigate();

	const handleClick = () => {
		actions.login(username,password);
		}
	
	
	if(store.token && store.token != "" && store.token != undefined) navigate("/")
	return (
		<div className="text-center mt-5">
			<h1>Login</h1>
			{(store.token && store.token != "" && store.token != undefined) ? "You are looged in with this token" + store.token :
			<div>

				<input type="text" placeholder="username" value={username} onChange={(e) => setUsername(e.target.value)}></input>
				<input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)}></input>
				<button onClick={handleClick}>Login</button>
			</div>
			}
		</div>
	);
};
