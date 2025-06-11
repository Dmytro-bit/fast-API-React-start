import {useLoaderData} from "react-router-dom";
import CarCard from "../components/CarCard.jsx";

const SingleCar = () => {
    const car = useLoaderData()
    return (
        <CarCard car={car}/>
    )
}

export default SingleCar