from config import link_list
import requests


def namer(link:str) -> str:
    """
    In the download function,
    it helps the file handler to do the file naming.
    
    Returns:
        str: name of file
    """
    name = ''
    for i in link[-1::-1]:
        if i == '/':
            break
        name += i
    name = name[-1::-1]
    return name


def downlod(addrs:str) -> None:
    """
    If the link is to a file (photo, audio),
      it will download that file.

    Args:
        addrs (str): File Link
    """
    name = namer(addrs)
    respons = requests.get(addrs)
    with open(name,"wb") as file:
        file.write(respons.content)
    if respons.ok:
        print(f'{name} Successful ')
    else:
        print(f'{name} Failed ')


if __name__ == "__main__":
    for i in link_list:
        downlod(i)
