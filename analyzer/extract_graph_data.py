import cv2
import numpy as np

def extract_graph_data(image_path):
    # Read the image
    img = cv2.imread(image_path, 0)

    # Pre-process the image (blurring, edge detection, etc.)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours of the graph
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract coordinates (or more sophisticated image analysis)
    graph_points = []
    for contour in contours:
        for point in contour:
            graph_points.append(point[0])

    # Return data points (this should be converted to meaningful graph data)
    return np.array(graph_points)

def analyze_data(data_points):
    # Find minima and maxima
    maxima = np.argmax(data_points, axis=0)
    minima = np.argmin(data_points, axis=0)

    return minima, maxima