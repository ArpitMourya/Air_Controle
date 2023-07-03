import customtkinter
import os
from PIL import Image
import pickle
# import HandGesture

global optionmenu_var
global task
global master_task_list
global static_task_ges
global dynamic_task_ges
global two_step_task_ges
#global dic_task_ges
optionmenu_var=[]
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
static_ges_img=["open_palm.jpg","thumbs_up.jpg","victory.jpg","L_gesture.jpeg"]
Two_step_ges_img = ["gun_shot.jpg","pointing_up.jpg"]
dynamic_ges_img =["C_gesture.jpeg","yoo.jpeg"]

static_ges_task=["None","CloseTab","ToggleTab","StopDetection"]
static_ges_master_task =["None","CloseTab","ToggleTab","StopDetection"]

Two_step_ges_task=["None","mousePointer","Scroll"]
Two_step_ges_master_task =["None","mousePointer","Scroll"]

dyanamic_ges_task=["None","Brightness","Volume"]
dyanamic_ges_master_task =["None","Brightness","Volume"]
static_task_ges={}
dynamic_task_ges={}
two_step_task_ges={}
im_id = []
static_gesture=[]
two_step_gesture=[]
dynamic_gesture=[]
selected_static=[]
selected_two_step=[]
selected_dynamic=[]
static_ges=["open_palm","thumbs_up","victory","L_gesture"]
Two_step_ges=["gun_shot","pointing_up"]
dynamic_ges=["C_gesture","yoo"]
# static_avail_gest=["open_palm","thumbs_up","victory","L_gesture"]
# dynamic_avail_gest=["gun_shot","pointing_up"]
# two_step_avail_gest=["C_gesture","yoo"]
global dic_task_ges

#to save settings permanent in computer
class MyClass():
    def __init__(self, static,two_step,dynamic):
        self.static = static
        self.two_step = two_step
        self.dynamic = dynamic
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


#to get the changed tasks
def change_static_task(set_task):
    global static_task_ges
    if set_task != "None":
        selected_static.append(set_task)
    # static_ges_task= [x for x in static_ges_master_task if x not in selected_static]
    optionmenu_var = [ges.get() for ges in static_gesture]
    for j in static_gesture :
        j.configure(app.home_frame, values=static_ges_task)
    static_task_ges= dict(zip(static_ges,optionmenu_var))
    # print(static_task_ges,two_step_task_ges,dynamic_task_ges,sep="\n",end="\n\n")
    obj=MyClass(static_task_ges,two_step_task_ges,dynamic_task_ges)
    save_object(obj)

def change_two_step_task(set_task):
    global two_step_task_ges
    if set_task != "None":
        selected_two_step.append(set_task)
    # Two_step_ges_task= [x for x in Two_step_ges_master_task if x not in selected_two_step]
    optionmenu_var = [ges.get() for ges in two_step_gesture]
    for j in two_step_gesture :
        j.configure(app.home_frame, values=Two_step_ges_task)
    two_step_task_ges= dict(zip(Two_step_ges,optionmenu_var))
    # print(static_task_ges,two_step_task_ges,dynamic_task_ges,sep="\n",end="\n\n")
    obj=MyClass(static_task_ges,two_step_task_ges,dynamic_task_ges)
    save_object(obj)
def change_dynamic_task(set_task):
    global dynamic_task_ges
    if set_task != "None":
        selected_dynamic.append(set_task)
    # dyanamic_ges_task= [x for x in dyanamic_ges_master_task if x not in selected_dynamic]
    optionmenu_var = [ges.get() for ges in dynamic_gesture]
    for j in dynamic_gesture :
        j.configure(app.home_frame, values=dyanamic_ges_task)
    dynamic_task_ges= dict(zip(dynamic_ges,optionmenu_var))
    # print(static_task_ges,two_step_task_ges,dynamic_task_ges,sep="\n",end="\n\n")
    obj=MyClass(static_task_ges,two_step_task_ges,dynamic_task_ges)
    save_object(obj)       
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Air Control")
        self.geometry("1400x750")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "handshake.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "gun_shot.jpg")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Air Control", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.getting_started_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Getting Started",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.getting_started_event)
        self.getting_started_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System","Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(3, weight=1)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        #create getting started framer
        self.getting_started_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.getting_started_button.configure(fg_color=("gray75", "gray25") if name == "Getting_Started" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Getting_Started":
            self.getting_started_frame(row=0, column=1, sticky="nsew")
        else:
            self.getting_started_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def getting_started_event(self):
        self.select_frame_by_name("getting_started_frame")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
if __name__ == "__main__":
    obj= load_object("data.pickle")
    # print(obj.static , obj.two_step,obj.dynamic,sep="\n")
    static_task_ges=obj.static
    two_step_task_ges = obj.two_step
    dynamic_task_ges = obj.dynamic

    app = App()
    #for static gestures
    for id,im in enumerate(static_ges_img,1):
        app.id = customtkinter.CTkImage(Image.open(os.path.join(image_path, im)), size=(150, 150))
        app.home_frame_large_image_label = customtkinter.CTkLabel(app.home_frame, text="", image=app.id)
        app.home_frame_large_image_label.grid(row=id, column=0, padx=10, pady=10)
    for id,option in enumerate(static_ges):
        optionmenu_var = customtkinter.StringVar(value=static_task_ges[option])
        option_menu = customtkinter.CTkOptionMenu(app.home_frame,state="None",variable=optionmenu_var, values=static_ges_task, command=change_static_task,)
        static_gesture.append(option_menu)
        option_menu.grid(row=id+1, column=1, padx=10, pady=(10, 20))

    #for two step
    for id,im in enumerate(Two_step_ges_img,1):
        app.id = customtkinter.CTkImage(Image.open(os.path.join(image_path, im)), size=(150, 150))
        app.home_frame_large_image_label = customtkinter.CTkLabel(app.home_frame, text="", image=app.id)
        app.home_frame_large_image_label.grid(row=id, column=2, padx=80, pady=10)
    for id,option in enumerate(Two_step_ges):
        optionmenu_var = customtkinter.StringVar(value=two_step_task_ges[option])
        option_menu = customtkinter.CTkOptionMenu(app.home_frame,state="None",variable=optionmenu_var, values=Two_step_ges_task, command=change_two_step_task)
        two_step_gesture.append(option_menu)
        option_menu.grid(row=id+1, column=3, padx=0, pady=(0, 0))

    #for dynamic
    for id,im in enumerate(dynamic_ges_img,1):
        app.id = customtkinter.CTkImage(Image.open(os.path.join(image_path, im)), size=(150, 150))
        app.home_frame_large_image_label = customtkinter.CTkLabel(app.home_frame, text="", image=app.id)
        app.home_frame_large_image_label.grid(row=id, column=4, padx=60, pady=40)
    
    for id,option in enumerate(dynamic_ges):
        optionmenu_var = customtkinter.StringVar(value=dynamic_task_ges[option])
        option_menu = customtkinter.CTkOptionMenu(app.home_frame,state="None",variable=optionmenu_var, values=dyanamic_ges_task, command=change_dynamic_task)
        dynamic_gesture.append(option_menu)
        option_menu.grid(row=id+1, column=5, padx=10, pady=(10, 20))
    app.mainloop()
