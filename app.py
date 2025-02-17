from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    colleges = []
    
    # Define categories and courses
    categories = ["GOPEN", "GSC", "GSEBC", "LOPEN", "LST", "LOBC", "EWS", "GST", "GOBC", "LSEBC", "LSC",
                  "GNTA", "GNTB", "GNTC", "DEFR-OBC", "PWDR-OBC", "LNTA", "LNTC", "LNTD", "PWD-O", "DEF-O",
                  "LNTB", "GNTD", "MI", "ORP", "PWDR-SC", "DEFR-SC", "DEFR-SEBC", "PWDR-SEBC", "DEFR-ST",
                  "DEFR-NTB", "DEFR-NTA"]

    courses = ['5G', 'Aeronautical Engineering', 'Agricultural Engineering', 'Artificial Intelligence', 'Artificial Intelligence (AI) and Data Science', 'Artificial Intelligence and Data Science', 'Artificial Intelligence and Machine Learning', 'Automation and Robotics', 'Automobile Engineering', 'Bio Medical Engineering', 'Bio Technology', 'Chemical Engineering', 'Civil Engineering', 'Civil Engineering and Planning', 'Civil and Environmental Engineering', 'Civil and infrastructure Engineering', 'Computer Engineering', 'Computer Engineering (Software Engineering)', 'Computer Engineering[Direct Second Year Second Shift]', 'Computer Science', 'Computer Science and Business Systems', 'Computer Science and Design', 'Computer Science and Engineering', 'Computer Science and Engineering (Artificial Intelligence and Data Science)', 'Computer Science and Engineering (Artificial Intelligence)', 'Computer Science and Engineering (Cyber Security)', 'Computer Science and Engineering (Internet of Things and Cyber Security Including Block Chain Technology)', 'Computer Science and Engineering (IoT)', 'Computer Science and Engineering(Artificial Intelligence and Machine Learning)', 'Computer Science and Engineering(Cyber Security)', 'Computer Science and Engineering(Data Science)', 'Computer Science and Information Technology', 'Computer Science and Technology', 'Computer Technology', 'Cyber Security', 'Data Engineering', 'Data Science', 'Electrical Engg [Electrical and Power]', 'Electrical Engg[Electronics and Power]', 'Electrical Engineering', 'Electrical and Computer Engineering', 'Electrical and Electronics Engineering', 'Electronics Engineering', 'Electronics Engineering ( VLSI Design and Technology)', 'Electronics and BiomedicalÂ Engineering', 'Electronics and Communication (Advanced Communication Technology)', 'Electronics and Communication Engineering', 'Electronics and Communication(Advanced Communication Technology)', 'Electronics and Computer Engineering', 'Electronics and Computer Science', 'Electronics and Telecommunication Engg', 'Electronics and Telecommunication Engg[Direct Second Year Second Shift]', 'Fashion Technology', 'Food Technology', 'Food Technology And Management', 'Industrial IoT', 'Information Technology', 'Instrumentation Engineering', 'Instrumentation and Control Engineering', 'Internet of Things (IoT)', 'Man Made Textile Technology', 'Manufacturing Science and Engineering', 'Mechanical & Automation Engineering', 'Mechanical Engineering', 'Mechanical Engineering[Sandwich]', 'Mechanical and Mechatronics Engineering (Additive Manufacturing)', 'Mechatronics Engineering', 'Metallurgy and Material Technology', 'Mining Engineering', 'Oil Fats and Waxes Technology', 'Oil Technology', 'Paints Technology', 'Paper and Pulp Technology', 'Petro Chemical Engineering', 'Petro Chemical Technology', 'Plastic Technology', 'Plastic and Polymer Engineering', 'Plastic and Polymer Technology', 'Printing Technology', 'Production Engineering', 'Production Engineering[Sandwich]', 'Robotics and Artificial Intelligence', 'Robotics and Automation', 'Safety and Fire Engineering', 'Structural Engineering', 'Surface Coating Technology', 'Textile Chemistry', 'Textile Engineering / Technology', 'Textile Plant Engineering', 'Textile Technology', 'VLSI']

    if request.method == "POST":
        student_score = float(request.form["score"])
        student_category = request.form["category"]
        desired_course = request.form["course"]

        # Connect to SQLite database
        conn = sqlite3.connect("colleges.db")
        cursor = conn.cursor()

        # SQL query with parameterized values
        query = f"""
            SELECT Institute, Course, {student_category} 
            FROM cutoffs 
            WHERE {student_category} <= ? 
            AND Course = ?
        """

        cursor.execute(query, (student_score, desired_course))

        # Fetch results
        results = cursor.fetchall()
        if results:
            for row in results:
                colleges.append(row)
        else:
            colleges.append("No matching colleges found.")

        # Close the connection
        conn.close()

    return render_template("index.html", colleges=colleges, categories=categories, courses=courses)

if __name__ == "__main__":
    app.run(debug=True)