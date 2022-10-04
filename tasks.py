import warnings
warnings.filterwarnings("ignore")


class tasks():

  
  daily_tasks = {}
  coming_tasks = {}
  scheduled_tasks = {}

  def __init__(self):
    pass
      
      
  def daily_task(self,id,temp):
    time = temp[temp.index('-daily')+1]

    # Checks for titl and description
    if '-title' in temp:
      title = temp[temp.index('-title')+1]
    else:
      title = 'No titled'

    if '-des' in temp:
      des = temp[temp.index('-des')+1]
    else:
      des = None


    # Checks if the time already in dict
    try:
      self.daily_tasks[time]
    except:
      self.daily_tasks.update({time : { id : 
                                       { 'Title' : title , 
                                        'Description' : des }
                                      }})
    else :
      self.daily_tasks[time].update({ id : 
                                       { 'Title' : title , 
                                        'Description' : des } 
                                      })
    print(self.daily_tasks)