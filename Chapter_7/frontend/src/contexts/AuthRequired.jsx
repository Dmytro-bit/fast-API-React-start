import {Navigate, Outlet} from "react-router-dom";
import {useAuth} from "../hooks/useAuth.jsx";

const AuthRequired = () => {
    const {jwt} = useAuth()

    return (
        <div>
            <h1>AuthRequired</h1>
            {jwt ? <Outlet/> : <Navigate to="/login"/>}
        </div>
    )
}

export default AuthRequired;