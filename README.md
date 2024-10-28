- **¿Qué ocurre si su API devuelve un error 500? ¿Cuál es el cuerpo del JSON en la respuesta?**  
  En caso de que la API devuelva un código de estado 500, se maneja una excepción indicando un error en el servidor. Esto suele ocurrir debido a un fallo interno, como un problema de base de datos o un error en la lógica de negocio del servidor. El JSON en la respuesta puede proporcionar detalles adicionales para el diagnóstico del error.

  ![image](https://github.com/user-attachments/assets/e7fbcfbe-f94d-4bc7-89cb-d3bd0b8bf95f)

- **¿Qué ocurre si su API devuelve un error 400? ¿Cuál es el cuerpo del JSON en la respuesta?**  
  En caso de un código de estado 400, se maneja una excepción que indica un error del cliente, por ejemplo, al solicitar un recurso que no existe. En este caso, se muestra un mensaje de "Pokémon no encontrado" en el cuerpo del JSON de la respuesta, proporcionando claridad al cliente sobre el motivo del error.

  ![image](https://github.com/user-attachments/assets/6049944b-66d9-425e-a110-55bb2cdd52f4)

