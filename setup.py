from  setuptools import find_packages,setup



def get_req(path:str):
    req=[]
    hypen_e_dot='-e .'
    with open(path,'r') as file:
        
        content=file.readlines()
        for i in content:
            z=i.replace("\n",'')
            req.append(z)
    
        if hypen_e_dot in req:
            req.remove(hypen_e_dot)  
    
    return req
    
    


setup(
    version='1.0',
    author='Amandeep',
    author_email='amandeepsingh.kaillay@gmail.com',
    name='Flight_price_prediction',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)