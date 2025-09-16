/* 2025 - Nuru Dashdamirli */

#include <zipfile.h>

extern "C" int init_embedded_py_module(char* module_name, char* module_code);

int zipModuleSearchOrLoad(char* module_name, TBool searchMode = EFalse) {
    // Connect to the Symbian file server
    RFs fileSession;
    User::LeaveIfError(fileSession.Connect());
    CleanupClosePushL(fileSession);

    // Dynamic UID handling for ZIP file
    TBuf<40> zipPath;
    TUid pythonAppUid = RProcess().SecureId();
    // dont forget to bundle the "module.zip" file in private directory!
    _LIT(zipFilePathTemplate, "\\private\\%08x\\module.zip");
    zipPath.Format(zipFilePathTemplate, pythonAppUid.iUid);
    
    // Open the ZIP file
    CZipFile* zipFile = CZipFile::NewL(fileSession, zipPath);
    CleanupStack::PushL(zipFile);
    
    // Construct the full file name inside the zip, e.g., "contacts.py"
    TBuf<30> moduleFileName;
    TInt cnt = 0;
    TChar c;
    while (c = module_name[cnt]) { // not ideal approach but saves memory
    	moduleFileName.Append(c);
    	cnt++;
    }
    moduleFileName.Append(_L(".py"));

    // Find the entry for the specific Python file
    CZipFileMember* member = zipFile->CaseInsensitiveMemberL(moduleFileName);
    CleanupStack::PushL(member);
    
    // if only search supposed to happen
    if (searchMode) {
        int result = (member == NULL)? 0 : 1;        
        CleanupStack::PopAndDestroy(3); // member, zipFile, moduleNameBuf, fileSession
        return result;
    }
    
    // Get an input stream for the zip member and read the data from it
    RZipFileMemberReaderStream* readerStream;
    zipFile->GetInputStreamL(member, readerStream);
    CleanupStack::PushL(readerStream);
    
    // read file into buffer
    TUint32 uncompressed_file_size = member->UncompressedSize();
    HBufC8* buffer = HBufC8::NewLC(uncompressed_file_size + 1);
    TPtr8 bufferPtr(buffer->Des());
    User::LeaveIfError(readerStream->Read(bufferPtr, uncompressed_file_size));
    bufferPtr.ZeroTerminate(); // important to terminate with NULL

    // load module in the buffer
    int result = init_embedded_py_module(module_name, (char *)bufferPtr.Ptr());
    CleanupStack::PopAndDestroy(5); // readerStream, fileContent, member, zipFile, moduleNameBuf, fileSession
    return result;
}

#define DEBUG_MODE

#ifdef DEBUG_MODE
#include <eikenv.h>
#include <eikinfo.h>

// A function to show a general info note
void ShowInfoNote(const TDesC& aMessage)
    {
    CEikonEnv::Static()->InfoMsg(aMessage);
    }
#endif


extern "C" int load_module_from_zip(char* module_name)
{
	int result;
    TRAPD(error, result = zipModuleSearchOrLoad(module_name, EFalse));

    if (error != KErrNone)
        {
#ifdef DEBUG_MODE
    	_LIT(KMyInfoMsg, "TEST ERROR load_module_from_zip");
    	ShowInfoNote(KMyInfoMsg);
#endif  	
        RDebug::Printf("Error initializing custom zip importer: %d", error);
		result = 0; //????
        }

	return result;
}

extern "C" int is_in_modules_zip(char* module_name)
{
	int result;
    TRAPD(error, result = zipModuleSearchOrLoad(module_name, ETrue));

    if (error != KErrNone)
        {
#ifdef DEBUG_MODE
    	_LIT(KMyInfoMsg, "TEST ERROR is_in_modules_zip");
    	ShowInfoNote(KMyInfoMsg);
#endif
        RDebug::Printf("Error initializing custom zip importer: %d", error);
        result = 0; //????
        }

	return result;
}

