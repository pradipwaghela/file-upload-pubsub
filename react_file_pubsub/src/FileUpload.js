import React, { useState } from "react";
import axios from "axios";

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("No upload yet");
    const [eventSource, setEventSource] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const uploadFile = async () => {
        if (!file) {
            alert("Please select a file to upload.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        setStatus("Uploading...");

        try {
            // Step 1: Upload the file
            const response = await axios.post("http://localhost:5000/upload", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });

            const { upload_id } = response.data;
            console.log("Upload started, ID:", upload_id);

            // Step 2: Start listening for upload progress
            startListening(upload_id);
        } catch (error) {
            console.error("Upload error:", error);
            setStatus("Upload failed.");
        }
    };

    const startListening = (uploadId) => {
        if (eventSource) {
            eventSource.close(); // Close any existing event source
        }

        const newEventSource = new EventSource(`http://localhost:5000/status/${uploadId}`);

        newEventSource.addEventListener (uploadId,(event) => {
            const data = event.data;
            console.log("Received update:", data);
            setStatus(data);

            // Close the connection if upload is completed
            if (data === "Completed") {
                newEventSource.close();
                setEventSource(null);
            }
        });

        newEventSource.onerror = (error) => {
            console.error("EventSource error:", error);
            setStatus("Error receiving updates");
            newEventSource.close();
        };

        setEventSource(newEventSource);
    };

    return (
        <div style={{ textAlign: "center", padding: "20px" }}>
            <h2>File Upload with Real-Time Progress</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={uploadFile} style={{ marginLeft: "10px" }}>Upload</button>
            <h3>Status: {status}</h3>
        </div>
    );
};

export default FileUpload;
