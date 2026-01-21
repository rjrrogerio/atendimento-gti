# Node.js User Creation System for Active Directory

This is a rewrite of the Python/Django application in Node.js/Express.

## Prerequisites

- Node.js (v14 or higher recommended)
- npm

## Installation

1. Navigate to the project directory:
   ```bash
   cd node_app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the server:
   ```bash
   node server.js
   ```

2. Open your browser and navigate to `http://localhost:3000`.

## Project Structure

- `server.js`: Main application entry point, handles routes and logic.
- `views/`: EJS templates (views).
- `public/`: Static assets (CSS, JS, images).
- `utils/`: Utility scripts (e.g., script generation logic).
- `data/`: Mock data (e.g., Unidades).

## Features

- Generates PowerShell scripts for creating AD users.
- Replicates the core functionality of the original Django app.
