import {createContext, useEffect, useState} from 'react';

export const AuthContext = createContext();
export const AuthProvider = ({children}) => {
    const [user, setUser] = useState(null);
    const [jwt, setJwt] = useState(localStorage.getItem('jwt') || null);
    const [message, setMessage] = useState("Please log in");

    useEffect(() => {
        const storedJwt = localStorage.getItem('jwt') || null;
        if (storedJwt) {
            setJwt(storedJwt);
            fetch(`${import.meta.env.VITE_API_URL}/users/me`, {
                headers: {Authorization: `Bearer ${storedJwt}`,},
            })
                .then(res => res.json()).then(data => {
                if (data.username) {
                    setUser({user: data.username});
                    setMessage(`Welcome back, ${data.username}!`);
                } else {
                    localStorage.removeItem('jwt');
                    setJwt(null);
                    setUser(null);
                    setMessage(data.message)
                }
            })
                .catch(() => {
                    localStorage.removeItem('jwt');
                    setJwt(null);
                    setUser(null);
                    setMessage('Please log in or register');
                });
        } else {
            setJwt(null);
            setUser(null);
            setMessage('Please log in or register');
        }
    }, []);

    const login = async (username, password) => {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/users/login`, {
            method: "POST",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify({username, password})
        });

        const data = await response.json()
        if (response.ok) {
            setJwt(data.token)
            localStorage.setItem("jwt", data.token)
            setUser(data.username)
            setMessage(`Log-in successful: welcome ${data.username}`)
        } else {
            setMessage("Login failed")
            setJwt(null)
            setUser(null)
            localStorage.removeItem("jwt")
        }
        return data
    }

    const logout = () => {
        setUser(null)
        setJwt(null)
        localStorage.removeItem('jwt')
        setMessage("Logout successful")
    }
    return (
        <AuthContext.Provider value={{user, jwt, login, logout, message, setMessage}}>
            {children}
        </AuthContext.Provider>
    )
};


