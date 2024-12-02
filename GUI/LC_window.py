import tkinter as tk

from GUI import LoginPage, RoosterMatch, StudentCourseOverviewPage, StudentOverviewPage, NewStudentPage, \
    ManageCoursesPage


class LC_window(tk.Tk):

    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args,**kwargs)
        # adding a title to the window
        self.wm_title("SchoolTools")
        self.geometry("1000x800")
        #remove after program is ready
        def donothing():
            print("kjlmjm")
        self.controller = controller
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        algemeenmenu = tk.Menu(menubar, tearoff=1)
        smartschoolmenu = tk.Menu(menubar, tearoff=2)
        algemeenmenu.add_command(label="RoosterMatch", command=lambda: self.show_frame(RoosterMatch.RoosterMatch))
        #filemenu.add_command(label="New Student", command=lambda: self.show_frame(NewStudentPage.NewStudentPage))
        #filemenu.add_command(label="Manage Courses", command=lambda: self.show_frame(ManageCoursesPage.ManageCoursesPage))
        #filemenu.add_command(label="Save", command=donothing)
        #filemenu.add_command(label="Save as...", command=donothing)
        #filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Algemeen", menu=algemeenmenu)
        menubar.add_cascade(label="Smartschool", menu=smartschoolmenu)
        self.config(menu=menubar)

        # creating a frame and assigning it to the container
        self.container = tk.Frame(self,height=1000,width=1000)
        # specifying the region where the frame is packed in root
        self.container.pack(side="top", fill="both",expand=True)

        # configuring the location of the container using grid
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)

        # create a dictionary of frames
        self.__frames = {}
        # adding the framecomponents to the frames
        for F in (RoosterMatch.RoosterMatch, StudentOverviewPage.StudentOverviewPage, ManageCoursesPage.ManageCoursesPage, StudentCourseOverviewPage.StudentCourseOverviewPage, NewStudentPage.NewStudentPage):
            frame = F(self.container, self)

            # the windows class acts as the root windows for the frames
            self.__frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        # using a method to switch frames
        self.show_frame(RoosterMatch.RoosterMatch)

    def show_frame(self, cont):
        frame = self.__frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def makeFilesIfNotExists(self):
        print("")