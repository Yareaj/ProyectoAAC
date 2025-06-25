# Proyecto AAC

Este proyecto consiste en un visualizador de aritmética en diferentes bases numéricas, con un backend en FastAPI y un frontend en React.

## Estructura del Proyecto

```
├── backend/              # API FastAPI
│   ├── main.py          # Archivo principal del backend
│   ├── requirements.txt # Dependencias Python
│   └── core/            # Módulos de lógica de negocio
├── frontend/            # Aplicación React
│   ├── src/             # Código fuente
│   └── package.json     # Dependencias Node.js
├── api/                 # Adaptador para Vercel
│   └── index.py         # Punto de entrada para serverless
├── vercel.json          # Configuración de Vercel
└── requirements.txt     # Dependencias Python para Vercel
```

## Desarrollo Local

Para ejecutar el proyecto localmente:

### Linux/macOS
```bash
# Terminal 1 - Backend
./run_backend.sh

# Terminal 2 - Frontend
./run_frontend.sh
```

### Windows
```cmd
# Terminal 1 - Backend
.\run_backend.bat

# Terminal 2 - Frontend  
.\run_frontend.bat
```

El frontend estará disponible en `http://localhost:5173` y se conectará automáticamente al backend en `http://localhost:8000` a través del proxy de Vite.

## Despliegue en Vercel

Este proyecto está configurado como un monorepo para desplegarse en Vercel:

1. **Frontend**: Se construye como una aplicación estática
2. **Backend**: Se despliega como funciones serverless en `/api/*`

### Configuración de Routing

- Las rutas de la API están disponibles en `/api/*`
- El frontend maneja todas las demás rutas
- En desarrollo, Vite proxies las llamadas a `/api` hacia `http://localhost:8000`
- En producción, Vercel enruta `/api` a las funciones serverless

### Variables de Entorno

El frontend detecta automáticamente si está en producción o desarrollo y ajusta las URLs de la API en consecuencia.

## Funcionalidades

- **Suma**: Visualización paso a paso de suma en base b
- **Resta**: Visualización paso a paso de resta en base b  
- **Multiplicación**: Visualización paso a paso de multiplicación en base b
- **Conversión**: Conversión entre bases numéricas

## Tecnologías

- **Backend**: FastAPI, Python, Pydantic
- **Frontend**: React, Vite, Tailwind CSS, Framer Motion
- **Despliegue**: Vercel (Monorepo)
