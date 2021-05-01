import sys
from .author import Author
from .projects import Package


def main():
  user = Author()


  param1 = sys.argv[1]

  if len(sys.argv) >= 3:
    project_name_input = sys.argv[2] 
    version_input = sys.argv[3] if len(sys.argv) == 4 else None

  if param1 == "init":
    user.update()
  elif param1.lower() == "new":
    pkg = Package(project_name_input, user, version_input)

    while True:
      test = input("Create with test folder ?(y/n)")
      
      if test.lower() == "y" and len(test.lower()) == 1:
        pkg.make(True)
        break
      elif test.lower() == "n" and len(test.lower()) == 1:
        pkg.make()
        break
      else:
        print("only (y) or (n)\n")
  

    
      

if __name__=="__main__":
  main()