from email import message
from email.mime import image
import facebook

image_url='https://document-export.canva.com/PklH0/DAE5MKPklH0/1/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220306%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220306T044635Z&X-Amz-Expires=7347&X-Amz-Signature=2bf71bce4089ba18d19e2849fb40761f85b80fcdb2bdcb9a2e44dc093128c7f6&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2006%20Mar%202022%2006%3A49%3A02%20GMT'

message="Gasken Murah"
link="https://www.colecall-media.id"
msg=message + "\n" + link

token=input("Enter Facebook Token Access=")
graph=facebook.GraphAPI(access_token=token)

# Facebook Id Group
id='373443873489539'

x=graph.put_object(id, 'photos', message=msg, url=image_url)
print(x)
print('Photo Sent Successfully')
