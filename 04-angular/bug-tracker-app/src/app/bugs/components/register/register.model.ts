export interface RegisterRequest {
    email : string,
    firstName : string,
    lastName : string,
    phoneNumber : string,
    password : string
//   public passwordConfirm : string = "";
}

export interface RegisterResponse {
    accessToken : string,
    user : User,
}
export interface User {
    email: string,
    firstname: string,
    lastname: string,
   
    phoneNumber: number
     
}