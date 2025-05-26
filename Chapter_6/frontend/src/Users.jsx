import {useEffect, useState} from "react";
import {useAuth} from "./AuthContext.jsx";

const Users = () => {
    const {jwt, logout} = useAuth()
    const [users, setUsers] = useState(null)
    const [error, setErrors] = useState(null)

    useEffect(() => {
        const fetchUsers = async () => {
            const response = await fetch("http://127.0.0.1:8000/users/list", {
                headers: {"Authorization": `Bearer ${jwt}`,},
            })

            const data = await response.json()
            if (!response.ok) {
                setErrors(data.detail)
            }
            setUsers(data.users)
        }
        if (jwt) {
            fetchUsers();
        }

    }, [jwt]);

    if (!jwt) return <div>Please log in to see all the users</div>;

    return (
        <div>
            {users ? (
                <div className="flex flex-col">
                    <h1>The list of users</h1>
                    <ol>
                        {users.map((user) => (
                            <li key={user.id}>{user.username}</li>
                        ))}
                    </ol>
                    <button onClick={logout} className="bg-blue-500 text-white  rounded">Logout</button>
                </div>
            ) : (
                <p>{error}</p>
            )}
        </div>
    );
}
export default Users