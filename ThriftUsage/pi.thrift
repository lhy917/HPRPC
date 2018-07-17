namespace py pi

struct PiRequest {
1:i32 n
}

struct PiResponse{
1:double value
}

exception IllegaArgument {
1: string message
}

service PiService {
    PiResponse cal(1:PiRequest req) throws(1:IllegaArgument ia)
}