import {useForm} from "react-hook-form"
import {z} from 'zod';
import {zodResolver} from '@hookform/resolvers/zod';
import {useAuth} from "../hooks/useAuth.jsx";

const schema = z.object({
    username: z.string().min(4, "Username must be at least 4 characters long")
        .max(10, "Username cannot exceed 10 characters"),
    password: z.string().min(4, "Password must be at least 4 characters long")
        .max(10, "Password cannot exceed 10 characters"),
});

const LoginForm = () => {
    const {register, handleSubmit, formState: {errors}} = useForm({
        resolver: zodResolver(schema),
    });
    const {login} = useAuth();

    const onSubmitForm = async (data) => {
        console.log(data)
        login(data.username, data.password)
    }

    return (
        <div className="flex items-center justify-center">
            <div className="w-full max-w-xs">
                <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" onSubmit={handleSubmit(onSubmitForm)}>

                    <div className="mb-4">
                        <label htmlFor="username"
                               className="block text-gray-700 text-sm font-bold mb-2">Username</label>
                        <input id="username" type="text" placeholder="Username" required {...register('username')}
                               className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"/>
                        {errors.username && <p className="text-red-500 text-xs italic">{errors.username.message}</p>}
                    </div>
                    <div className="mb-6">
                        <label htmlFor="password"
                               className="block text-gray-700 text-sm font-bold mb-2">Password</label>
                        <input id="password" type="password" placeholder="****" required {...register('password')}
                               className="shadow appearance-none border rounded w-fullpy-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"/>
                        {errors.password && <p className="text-red-500 text-xs italic">{errors.password.message}</p>}
                    </div>
                    <div className="flex items-center justify-between">
                        <button type="submit">Sign In</button>
                    </div>
                </form>
            </div>
        </div>
    )
}
export default LoginForm