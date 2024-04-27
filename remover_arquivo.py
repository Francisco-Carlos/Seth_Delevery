import  os

path = 'C:/Users/franc/OneDrive/Desktop/Seth/Seth_coxinha/static/img/Pagamento.png'

if os.path.isfile(path):
    os.remove(path)
else:
    # If it fails, inform the user.
    print("Error: %s file not found" % path)