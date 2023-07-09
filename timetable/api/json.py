# package controllers

# import (
# 	"fmt"

# 	"github.com/gin-gonic/gin"
# 	fluttermodels "github.com/wizely99/timetable/flutter_models"
# 	"github.com/wizely99/timetable/models"
# )

# func parseCourseToStruct(schedules []models.Schedule) []fluttermodels.MiniScheduleModel {
# 	daysOfWeek := []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# 	var scheduleList []fluttermodels.MiniScheduleModel
# 	for _, schedule := range schedules {
# 		miniScheduleModel := fluttermodels.MiniScheduleModel{
# 			WeekDay:   daysOfWeek[schedule.WeekDay],
# 			TimeRange: fmt.Sprintf("10:20 to 12:30"),
# 			Location:  schedule.Venue.Name,
# 		}
# 		scheduleList = append(scheduleList, miniScheduleModel)
# 	}
# 	return scheduleList
# }
# func (c *ClassController) GetClass(context *gin.Context) {
# 	class := models.Class{}
# 	classID := context.Param("id")
# 	jsonObj := make(map[string]interface{})

# 	db := preloadDb(c.db, c.model.PreloadFields())
# 	if err := db.Where("id = ?", classID).First(&class).Error; err != nil {
# 		fmt.Println(err)
# 		context.AbortWithStatus(404)
# 	}
# 	// general data from class to use in profile
# 	program := class.Program
# 	year := class.Year
# 	// add data to profile
# 	profileModel := fluttermodels.ProfileModel{
# 		ID:                 1,
# 		ProgrameCode:       class.Program,
# 		ProgrameName:       class.Program,
# 		RegistrationNumber: "2019-04-13442",
# 		PhoneNumber:        "0712121212",
# 		Email:              "wizely99@gmail.com",
# 	}
# 	// compose schedules and courses
# 	// starting with course
# 	var scheduleModels []fluttermodels.ScheduleModel

# 	var courseModels []fluttermodels.CourseModel
# 	for _, course := range class.Courses {
# 		CourseCode := course.Code
# 		CourseName := course.Name
# 		CourseID := course.ID
# 		Color := "#456123"
# 		for _, sched := range course.Schedules {
# 			scheduleModels = append(scheduleModels, fluttermodels.ScheduleModel{
# 				ID:         int(sched.ID),
# 				CourseID:   int(CourseID),
# 				CourseCode: CourseCode,
# 				Color:      Color,
# 				CourseName: CourseName,
# 				WeekDay:    sched.WeekDay,
# 				StartTime:  sched.StartTime.Format("15:04"),
# 				EndTime:    sched.EndTime.Format("15:04"),
# 				VenueName:  sched.Venue.Name,
# 				VenueCode:  sched.Venue.Code,
# 			})
# 		}

# 		courseModels = append(courseModels, fluttermodels.CourseModel{
# 			ID:          int(course.ID),
# 			Code:        course.Code,
# 			Name:        course.Name,
# 			Color:       "#123456",
# 			Credits:     8,
# 			Facilitator: course.Facilitator,
# 			Schedules:   parseCourseToStruct(course.Schedules),
# 		})

# 	}

# 	//load assignments

# 	// CONSIDERING ALL SCHEDULES
# 	jsonObj["program"] = program
# 	jsonObj["year"] = year
# 	jsonObj["profile"] = profileModel
# 	jsonObj["courseModels"] = courseModels
# 	jsonObj["scheduleModels"] = scheduleModels
# 	context.JSON(200, jsonObj)
# }
