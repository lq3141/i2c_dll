#ifdef CREATEDLL_EXPORTS
    #define CREATEDLL_API __declspec(dllexport)
#else
    #define CREATEDLL_API __declspec(dllimport)
#endif

extern "C"
{
	CREATEDLL_API int printtest();
}
