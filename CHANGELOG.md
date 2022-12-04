# 0.1.0

First version of `WSBLib`

## Major commits

- [5cb425a](https://github.com/firlast/wsblib/commit/5cb425a): Adding `Server` class;
- [690bcc2](https://github.com/firlast/wsblib/commit/690bcc2): Adding `Client` class;
- [4ea2d8c](https://github.com/firlast/wsblib/commit/4ea2d8c): Adding HTTP status code in `HTTPStatus` class;
- [4aa787e](https://github.com/firlast/wsblib/commit/4aa787e): Adding `Route` class;
- [fae9b41](https://github.com/firlast/wsblib/commit/fae9b41): Adding `ProcessRequest` class;
- [7b46cf9](https://github.com/firlast/wsblib/commit/7b46cf9): Creating `Response` object to callback return.

# 0.2.0

Adding the possibility to create **dynamic routes** and get data from parameters.

## Major commits

- [b27fdc1](https://github.com/firlast/wsblib/commit/b27fdc1): Adding `Route._register_dynamic_route` method;
- [5381ed2](https://github.com/firlast/wsblib/commit/5381ed2): Adding `Route.get_parameters` method;
- [e238029](https://github.com/firlast/wsblib/commit/e238029): Adding `RequestData` class;
- [2ef5768](https://github.com/firlast/wsblib/commit/2ef5768): Creating `RequestData` instance to store request data.

# 0.3.0

Adding module to log request data and returning request data in `ProcessRequest.process`.

## Major commits

- [f69dd0d](https://github.com/firlast/wsblib/commit/f69dd0d): Returning request data in `ProcessRequest.process` method;
- [3ac316b](https://github.com/firlast/wsblib/commit/3ac316b): Creating `RequestData` instance outside condition;
- [ba271f7](https://github.com/firlast/wsblib/commit/ba271f7): Adding `log_request` function;

# 0.4.0

Adding HTTP status error handler.

## Major commits

- [202b064](https://github.com/firlast/wsblib/commit/202b064): Checking route parameters in `Route.match_route` method;
- [c59de99](https://github.com/firlast/wsblib/commit/c59de99): Adding `Error` class to handle http status code errors;
- [6ee1e28](https://github.com/firlast/wsblib/commit/6ee1e28): Renaming exception to `InvalidResponseError`;
- [fff0eb7](https://github.com/firlast/wsblib/commit/fff0eb7): Adding errors callback in request process.

# 0.5.0

Making request data available from the function's global variables.

## Major commits

- [e180e05](https://github.com/firlast/wsblib/commit/e180e05): Making request data available through global variables;
- [81e1743](https://github.com/firlast/wsblib/commit/81e1743): Passing `use_globals` argument to `get_route_response` method.

# 0.6.0

Adding `Server.destroy` method to close server socket.

## Major commits

- [b0eca90](https://github.com/firlast/wsblib/commit/b0eca90): Adding `destroy` method to Server class;
- [da812a3](https://github.com/firlast/wsblib/commit/da812a3): Destroying soket in unit test.

# 0.7.0

Adding `RequestData.json` method to convert a **JSON** body in `dict`.

## Major commits

- [7257af3](https://github.com/firlast/wsblib/commit/7257af3): Adding method to convert JSON body to dict;
- [c239ab2](https://github.com/firlast/wsblib/commit/c239ab2): Fix change log.

# 1.0.0

Providing **full control** of the *request and response* cycle to the customer.

## Major commits

- [c388264](https://github.com/firlast/wsblib/commit/c388264): Create `RequestProcessed` class;
- [5e4d610](https://github.com/firlast/wsblib/commit/5e4d610): Create `RequestProcessed` instance and returning;
- [51d42a0](https://github.com/firlast/wsblib/commit/51d42a0): Removing `use_globals` parameter from `ProcessRequest.process` method;
- [3ccc832](https://github.com/firlast/wsblib/commit/3ccc832): Adding method to get route by path;
- [dc35cd0](https://github.com/firlast/wsblib/commit/dc35cd0): Setting "parameter" attribute only when route is found;
- [9fa9dec](https://github.com/firlast/wsblib/commit/9fa9dec): Adding default errors list;
- [64fd9d3](https://github.com/firlast/wsblib/commit/64fd9d3): Extend `errors_callback` list with `default_errors`.

# 1.1.0

Making it easier to get the response from the route or callback function.

## Major commits

- [9728988](https://github.com/firlast/wsblib/commit/9728988): Adding method to get response from callback or route; 
- [cc85253](https://github.com/firlast/wsblib/commit/cc85253): Receiving `use_globals` argument in `get_response` method.

# 1.1.1

Print query string in log request.

## Major commits

- [828973d](https://github.com/firlast/wsblib/commit/828973d): Include query string in request path.

# 1.1.2

Update project requirements.

## Major commits

- [50b4b9e](https://github.com/firlast/wsblib/commit/50b4b9e): Update project requires.
