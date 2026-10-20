# Evaluación práctica — Versión 25: Productora de eventos

Gestión de solicitudes en memoria usando estructuras propias en Python:

- **Lista enlazada**: registra las solicitudes (EV01 Sonido, EV02 Luces, EV03 Escenario); `agregar` inserta al final sin perder nodos.
- **Pila (LIFO)**: `apilar` / `desapilar`, controla pila vacía.
- **Cola (FIFO)**: `encolar` / `desencolar`, controla cola vacía.
- **Reto individual**: se verifica que *deshacer* (desapilar) no borra el registro de la lista enlazada.

## Ejecución

```
python ProductoradeEventos.py
```

No usa bases de datos ni librerías externas.
