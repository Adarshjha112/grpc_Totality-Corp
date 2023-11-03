import grpc
import user_service_pb2
import user_service_pb2_grpc
from concurrent import futures  # Import the futures module

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def GetUserByID(self, request, context):
        # Implement logic to fetch user by ID from your list
        user = find_user_by_id(request.user_id)
        if user:
            return user_service_pb2.UserResponse(**user)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return user_service_pb2.UserResponse()

    def GetUsersByIDs(self, request, context):
        for user_id in request.user_ids:
            user = find_user_by_id(user_id)
            if user:
                yield user_service_pb2.UserResponse(**user)

def find_user_by_id(user_id):
    # Implement logic to find the user in your data
    # Return the user as a dictionary
    pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
