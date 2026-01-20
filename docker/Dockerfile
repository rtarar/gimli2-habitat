# gimli2-habitat CadQuery environment
# For STEP file processing with OpenCASCADE

FROM mambaorg/micromamba:1.5.10

LABEL org.opencontainers.image.title="gimli2-habitat-cadquery"
LABEL org.opencontainers.image.description="CadQuery environment for STEP file processing"

# Install system dependencies for OpenCASCADE/OCP (requires root)
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglu1-mesa \
    libxrender1 \
    libxcursor1 \
    libxft2 \
    libxinerama1 \
    && rm -rf /var/lib/apt/lists/*
USER $MAMBA_USER

# Copy environment specification
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml

# Install packages into base environment and fix ezdxf version
# Note: conda-forge's cadquery has broken ezdxf dependency
ARG MAMBA_DOCKERFILE_ACTIVATE=1
RUN micromamba install --yes --file /tmp/environment.yml && \
    pip install --no-cache-dir "ezdxf>=1.0,<1.4" && \
    micromamba clean --all --yes

# Set working directory for mounted project files
WORKDIR /workspace

# Default entrypoint preserves conda activation
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]

# Default command
CMD ["python", "--version"]
