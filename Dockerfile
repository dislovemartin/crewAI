FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install hatchling for building the project
RUN pip install --upgrade pip hatchling

# Copy project files
COPY . /app

# Install project dependencies through the pyproject.toml
RUN pip install .

# Expose the port if necessary (assuming 8000, change if needed)
EXPOSE 8000

# Set the default command to run the crewai CLI
CMD ["crewai"] 