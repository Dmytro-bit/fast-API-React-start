import {createBrowserRouter, createRoutesFromElements, Route, RouterProvider} from "react-router-dom";
import './App.css'
import RootLayout from "./layouts/RootLayout.jsx";
import Cars, {carsLoader} from "./pages/Cars.jsx"
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx"
import NewCar from "./pages/NewCar.jsx"
import SingleCar from "./pages/SingleCar.jsx"
import NotFound from "./pages/NotFound.jsx"
import {AuthProvider} from "./contexts/AuthContext.jsx";
import AuthRequired from "./contexts/AuthRequired.jsx";
import fetchCarData from "./utils/fetchCarData"


const router = createBrowserRouter(
    createRoutesFromElements(
        <Route path="/" element={<RootLayout/>} errorElement={<NotFound/>}>
            <Route index element={<Home/>}/>
            <Route path="cars" element={<Cars/>} loader={carsLoader}/>
            <Route path="login" element={<Login/>}/>
            <Route element={<AuthRequired/>}>
                <Route path="new-car" element={<NewCar/>}/>
            </Route>
            <Route path="cars/:id" element={<SingleCar/>}
                   loader={async ({params}) => {
                       return fetchCarData(params.id)
                   }}

                   errorElement={<NotFound/>}
            />
        </Route>
    )
)


export default function App() {
    return (
        <AuthProvider>
            <RouterProvider router={router}/>
        </AuthProvider>
    )
}
