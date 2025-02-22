# 📄 FuturePrint Security Camera System - Full Report

**Author:** Mr. James Bishop  
**University:** University of Northampton  
**Course:** BSc (Hons) Computer Science  
**Module:** Media Technology 24/25  

**Graded:** 96/100 (A+)

---

## 📌 **Table of Contents**
1. [Introduction](#introduction)
2. [Research & Literature Review](#research--literature-review)
3. [Problem Analysis & Client Information](#problem-analysis--client-information)
4. [Project Design](#project-design)
5. [Project Implementation](#project-implementation)
6. [Application Testing](#application-testing)
7. [Project Evaluation](#project-evaluation)
8. [References](#references)

---

## 📖 **Introduction**
Crime rates in Northampton have been on the rise, with **112.3 crimes per 1,000 people** as of January 2025. FuturePrint LTD, a printing company, is at **risk of theft** due to valuable assets stored in its warehouse. This project aims to develop a **Python-based security camera system** to enhance surveillance and prevent potential break-ins.

---

## 🔬 **Research & Literature Review**
Security cameras **deter criminal activity** by increasing the risk of detection and prosecution. Key findings:
- **Tesco supermarkets** use **CCTV systems** to prevent shoplifting in high-risk areas (Cherruault, 2025).
- **Ring doorbells** helped **reduce burglaries by 55%** in Los Angeles (Undark, 2023).
- Concerns about **privacy & AI surveillance** (Sellman, 2024).

Crime statistics indicate that businesses with **high-value assets** are at greater risk, making security camera deployment **essential**.

---

## 🔍 **Problem Analysis & Client Information**
### About **FuturePrint LTD**
- 📍 Based in Northampton  
- 🏭 **11 employees** providing **printing services**  
- 💰 **£1M worth of equipment** at risk  

### Identified **Issues**
1. **Outdated Security System** - Cameras are **faulty** and lack **motion detection**.  
2. **No Video Logging** - No **saved footage** for reviewing break-ins.  
3. **Manual Surveillance** - Security **dependent on staff presence**.

### **Client Requirements**
✔️ **Live Camera Feeds** (Front Entrance & Warehouse)  
✔️ **Motion Detection & Logging**  
✔️ **Simultaneous Multi-Camera View**  
✔️ **Graphical User Interface (GUI)**  
✔️ **Video Compression for Storage Efficiency**  
✔️ **Error Handling for Camera Failures**  

---

## 🎨 **Project Design**
### 📊 **Graphical User Interface (GUI)**
- **Wireframe approved** by FuturePrint.
- Designed with **Tkinter** for simplicity.

### 🏗 **Functionality Design**
- **Flowchart** visualizing how the system processes motion detection.
- Motion **triggers recording** which stops **10 seconds after inactivity**.

---

## 🛠 **Project Implementation**
### 🎥 **Multiple Security Camera Feeds**
- Displays **both cameras simultaneously** to detect threats at **front & warehouse**.
- Uses **OpenCV** for video capture.

### 🎯 **Motion Detection & Tracking**
- Captures **two frames**, calculates **differences**, and **draws rectangles** around moving objects.

### 📂 **Saved Video Footage & Compression**
- **H.264 encoding** reduces file size.
- **Automatic saving** when motion is detected.

### 🖥 **Graphical User Interface**
- **Tkinter-based GUI** with:
  - ✅ Start/Stop Buttons
  - ✅ Multiple Camera Views
  - ✅ Motion Logging

### 📝 **Logging of Motion Events**
- **Time-stamped logs** to track detected motion.
- Stored in a **.txt log file**.

### 🕒 **Date/Time Overlay**
- **Live timestamp** displayed on each frame.

---

## 🧪 **Application Testing**
### ✅ **Test Cases & Results**
| Test Case | Expected Outcome | Result |
|-----------|----------------|--------|
| Camera Connectivity Error | Display warning message | ✅ Passed |
| Motion Detection | Detect and track movement | ✅ Passed |
| Video Saving | Store footage when motion is detected | ✅ Passed |
| GUI Buttons | Start/Stop functionality | ✅ Passed |
| CPU Usage | Efficient processing | ✅ Passed (75% CPU usage) |

---

## 📊 **Project Evaluation**
This project highlights the **importance of security measures** for businesses. It successfully integrates:
- **Python-based real-time surveillance**
- **Automated motion detection & tracking**
- **Efficient video storage & logging**

💡 **Future Enhancements**:
1. 📡 **Cloud Integration** for Remote Storage  
2. 🎭 **Face Recognition** to Detect Suspicious Individuals  
3. 📲 **Real-time Alerts via Mobile Notifications**  

---

## 📜 **References**
- **Plumplot (n.d.)**. Northampton crime statistics. [🔗 Link](https://www.plumplot.co.uk/Northampton-crime-stats.html)  
- **Cherruault, N. (2025)**. Tesco security upgrade. [🔗 Link](https://www.thescottishsun.co.uk/news/14190358/tesco-alcohol-security-upgrade/)  
- **Undark, R.M. (2023)**. Ring doorbells prevent crime. [🔗 Link](https://www.scientificamerican.com/article/do-video-doorbells-really-prevent-crime/)  
- **Sellman, M. (2024)**. AI and privacy concerns. [🔗 Link](https://www.thetimes.com/uk/technology-uk/article/network-rail-secretly-used-ai-to-read-passengers-emotions-nknvtj58n)  

---

🚀 **Developed by Mr. James Bishop for the University of Northampton - BSc (Hons) Computer Science**
