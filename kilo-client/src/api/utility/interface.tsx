// Interface for User
export interface User {
    id: number
    first_name: string;
    last_name: string;
    kilo_access: boolean;
    is_admin: boolean;
    _uuid: string;
}

// Interface for GetUsersResponse
export interface GetUsersResponse {
    users: User[];
}

//Interface for GetUserResponse
export interface GetUserResponse {
    qr_code: string;
    user: User;
}

// Interface for SigninResponse 
export interface SigninResponse {
    status: 200;
    access_token: string;
    refresh_token: string;
    user: User;
}

// Api Error interface if API fails
export interface ApiError {
    error: true;
    message: string;
}